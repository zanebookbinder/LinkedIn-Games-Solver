from readchar import readkey, key
from rich.console import Console
from web_scraper import WebScraper
from tango_solver import TangoSolver
from queens_solver import QueensSolver
from zip_solver import ZipSolver
import time


class Solver:

    game_to_solve_dict = {
        "Tango": TangoSolver,
        "Queens": QueensSolver,
        "Zip": ZipSolver,
    }

    def __init__(self):
        input_game = self.user_selects_game()
        if input_game not in Solver.game_to_solve_dict:
            print("Invalid game selected. Exiting...")
            exit(0)

        start_time = time.time()

        game_url = Solver.game_to_solve_dict[input_game].game_url
        web_scraper = WebScraper(game_url)
        driver = web_scraper.get_driver()
        game_solver = Solver.game_to_solve_dict[input_game](
            driver
        )  # gets board and transitions

        found_board_time = time.time()
        print(f"Took {found_board_time - start_time} to find board data")

        game_solver.solve_game()

        solved_game_time = time.time()
        print(f"Took {solved_game_time - found_board_time} to solve game")

        game_solver.print_solved_game()
        game_solver.add_solved_board_to_site(driver)

        added_solution_time = time.time()
        print(f"Took {added_solution_time - solved_game_time} to add solution to site")

        time.sleep(100)
        web_scraper.quit_driver()

    def user_selects_game(self):
        options = list(Solver.game_to_solve_dict.keys())
        selected = 0

        console = Console()
        while True:
            console.clear()
            console.print("[bold]Choose your game:[/bold]\n")

            for i, option in enumerate(options):
                if i == selected:
                    console.print(f"> [bold green]{option}[/bold green]")
                else:
                    console.print(f"  {option}")

            k = readkey()

            if k == key.UP:
                selected = (selected - 1) % len(options)
            elif k == key.DOWN:
                selected = (selected + 1) % len(options)
            elif k == key.ENTER:
                break

        return options[selected]


if __name__ == "__main__":
    Solver()
