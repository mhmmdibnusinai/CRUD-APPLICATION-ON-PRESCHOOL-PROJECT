
import pyinputplus as pyip
import CRUD

if __name__ == "__main__":
    CRUD.clear_screen()
    while True:
        CRUD.clear_screen()
        print(f"============={CRUD.greetings()}====================")
        print("-WELCOME TO TADIKA MESRA INFORMATION SYSTEM -")
        print("==============================================")

        print(f"1. Show student data")
        print(f"2. Add student data")
        print(f"3. Update student data")
        print(f"4. Delete student data")
        print(f'5. Exit terminal\n')

        Choose = pyip.inputInt("Choose 1-5: ", min=1, max=5, default=1)

        # Lakukan tindakan sesuai pilihan pengguna
        if Choose == 1:
            CRUD.Show()
        elif Choose == 2:
            CRUD.Add()
        elif Choose == 3:
            CRUD.Update()
        elif Choose == 4:
            CRUD.Delete()
        elif Choose == 5:
            exit = pyip.inputYesNo(prompt="Press 'ENTER' to close the terminal or (yes/no)", blank=True)
            if exit == "yes" or exit == "":
                CRUD.clear_screen()
                break
                