from django.shortcuts import render
import random

# globalna zmienna - liczba do zgadnięcia
secret_number = random.randint(1, 100)

def guess_number(request):
    message = ""
    global secret_number

    if request.method == "POST":
        try:
            guess = int(request.POST.get("guess"))
            if guess < secret_number:
                message = "📉 Za mało!"
            elif guess > secret_number:
                message = "📈 Za dużo!"
            else:
                message = f"🎉 Brawo! Trafiłeś! Liczba to {secret_number}"
                secret_number = random.randint(1, 100)  # nowa runda
        except (ValueError, TypeError):
            message = "❌ Podaj prawidłową liczbę!"

    return render(request, "main/game.html", {"message": message})
