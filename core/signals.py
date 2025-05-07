from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # GÜVENLİK: Profil zaten varsa tekrar oluşturmaz
            Profile.objects.get_or_create(user=user)

            try:
                group = Group.objects.get(name='Students of Mans')
                group.user_set.add(user)
            except Group.DoesNotExist:
                print("Hata: 'Students of Mans' grubu bulunamadı.")

            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})
