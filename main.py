from pet import Pet

def display_menu():
    """Show a colorful action menu."""
    print("\n" + "=" * 30)
    print("🛎️  What should your pet do?")
    print("1. Eat 🍗")
    print("2. Sleep 💤")
    print("3. Play 🎾")
    print("4. Train New Trick 🌟")
    print("5. Show Tricks 🎩")
    print("6. Check Status 📊")
    print("7. Exit 👋")
    print("=" * 30)

def main():
    print("""
    🐾~~~~~~~~~~~~~~~~~~~~~~~~~~~🐾
    Welcome to VIRTUAL PET SIMULATOR!
    🐾~~~~~~~~~~~~~~~~~~~~~~~~~~~🐾
    """)
    
    # Initialize pet
    pet_name = input("Name your pet: ").strip() or "Buddy"
    pet = Pet(pet_name)
    print(f"\nMeet {pet.name}! 🎉 A new pet is born!")

    # Main game loop
    while True:
        display_menu()
        choice = input("Choose (1-7): ").strip()

        if choice == '1':
            pet.eat()
        elif choice == '2':
            pet.sleep()
        elif choice == '3':
            pet.play()
        elif choice == '4':
            trick = input("What trick should they learn? ").strip()
            pet.train(trick)
        elif choice == '5':
            pet.show_tricks()
        elif choice == '6':
            pet.get_status()
        elif choice == '7':
            print(f"\n💌 {pet.name} waves goodbye! See you next time!")
            break
        else:
            print("❌ Invalid choice! Try 1-7.")

if __name__ == "__main__":
    main()