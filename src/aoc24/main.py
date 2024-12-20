"""Module that contains the `main` method.

This method is ran when the script is ran as a module and when it is ran as a
executable script.
"""

from rich.console import Console

from aoc.advent_of_code import AdventOfCode

from .solutions import (
    Day01,
    Day02,
    Day03,
    Day04,
    Day05,
    Day06,
    Day07,
    Day08,
    Day09,
    Day10,
    Day11,
    Day12,
    Day13,
    Day14,
)


def main() -> None:
    """Main function for the application."""
    aoc24 = AdventOfCode()
    console = Console()

    # Add solutions
    # aoc24.add_solution(1, Day01('data/day01-input.txt'))
    # aoc24.add_solution(2, Day02('data/day02-input.txt'))
    # aoc24.add_solution(3, Day03('data/day03-input.txt'))
    # aoc24.add_solution(4, Day04('data/day04-input.txt'))
    # aoc24.add_solution(5, Day05('data/day05-input.txt'))
    # aoc24.add_solution(6, Day06('data/day06-input.txt'))
    # aoc24.add_solution(7, Day07('data/day07-input.txt'))
    # aoc24.add_solution(8, Day08('data/day08-input.txt'))
    # aoc24.add_solution(9, Day09('data/day09-input.txt'))
    # aoc24.add_solution(10, Day10('data/day10-input.txt'))
    # aoc24.add_solution(11, Day11('data/day11-input.txt'))
    # aoc24.add_solution(12, Day12('data/day12-input.txt'))
    # aoc24.add_solution(13, Day13('data/day13-input.txt'))
    aoc24.add_solution(13, Day14('data/day14-input.txt', (101, 103)))

    # Print solutions
    console.print(
        '[yellow][bold]Advent of Code 2024 - Python version[/bold][/yellow]'
    )
    console.print('[gray]By Daryl Stark[/gray]')
    console.print('')
    for day in range(1, 25):
        solution = aoc24.get_solution(day)
        if solution is not None:
            console.print(f'[bold]Day {day:02}[/bold]: ', end='')
            console.print(f'Puzzle 1: {solution.solve_puzzle_one()}')
            console.print(
                ' ' * 8, f'Puzzle 2: {solution.solve_puzzle_two()}', sep=''
            )
