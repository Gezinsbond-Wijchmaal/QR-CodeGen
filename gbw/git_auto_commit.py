import subprocess

def run_command(command):
    """Voer een shell-commando uit en print de output live."""
    process = subprocess.Popen(command, shell=True)
    process.communicate()

def main():
    print("🔹 Automatisch Git Commit & Push Script 🔹")
    message = input("Voer je commit message in: ")

    if not message.strip():
        print("❌ Geen commit message opgegeven. Stoppen.")
        return

    print("\n➡️ Bestanden toevoegen...")
    run_command("git add .")

    print("\n➡️ Commit maken...")
    run_command(f'git commit -m "{message}"')

    print("\n➡️ Pushen naar GitHub...")
    run_command("git push origin main")

    print("\n✅ Klaar! Alle wijzigingen zijn gepusht naar GitHub.")

if __name__ == "__main__":
    main()
