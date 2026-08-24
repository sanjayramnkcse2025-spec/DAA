{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EeHPNHOx3gz2"
      },
      "outputs": [],
      "source": [
        "def is_safe(board, row, col):\n",
        "    for prev_row in range(row):\n",
        "        placed = board[prev_row]\n",
        "        if placed == col:  # Same column\n",
        "            return False\n",
        "        if abs(prev_row - row) == abs(placed - col):  # Diagonal\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "def solve_n_queens(n):\n",
        "    board     = [-1] * n\n",
        "    solutions = []\n",
        "    backtrack_count = [0]\n",
        "\n",
        "    def backtrack(row):\n",
        "        if row == n:\n",
        "            solutions.append(board[:])\n",
        "            return\n",
        "        for col in range(n):\n",
        "            if is_safe(board, row, col):\n",
        "                board[row] = col\n",
        "                backtrack(row + 1)\n",
        "                board[row] = -1  # Undo\n",
        "                backtrack_count[0] += 1\n",
        "\n",
        "    backtrack(0)\n",
        "    return solutions, backtrack_count[0]\n",
        "\n",
        "def display_board(solution, n):\n",
        "    print('  +' + '---+' * n)\n",
        "    for row in range(n):\n",
        "        print('  |', end='')\n",
        "        for col in range(n):\n",
        "            if solution[row] == col:\n",
        "                print(' Q |', end='')\n",
        "            else:\n",
        "                print(' . |', end='')\n",
        "        print()\n",
        "        print('  +' + '---+' * n)\n",
        "\n",
        "# --- Solve for N=4 (show all) and N=8 (count only) ---\n",
        "for n in [4, 6, 8]:\n",
        "    solutions, backtracks = solve_n_queens(n)\n",
        "    print(f'N={n}: {len(solutions)} solutions, {backtracks} backtracks')\n",
        "    if n == 4:\n",
        "        print(f'\\n  All solutions for {n}-Queens:')\n",
        "        for i, sol in enumerate(solutions, 1):\n",
        "            print(f'\\n  Solution {i}: {sol}')\n",
        "            display_board(sol, n)"
      ]
    }
  ]
}