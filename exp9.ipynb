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
        "id": "Y9iNPbSN5AHj"
      },
      "outputs": [],
      "source": [
        "def first_fit(items, capacity=1.0):\n",
        "    bins = []  # Each bin stores remaining space\n",
        "    bin_contents = []\n",
        "    for item in items:\n",
        "        placed = False\n",
        "        for i, space in enumerate(bins):\n",
        "            if space >= item:\n",
        "                bins[i] -= item\n",
        "                bin_contents[i].append(item)\n",
        "                placed = True\n",
        "                break\n",
        "        if not placed:\n",
        "            bins.append(capacity - item)\n",
        "            bin_contents.append([item])\n",
        "    return bin_contents\n",
        "\n",
        "def first_fit_decreasing(items, capacity=1.0):\n",
        "    return first_fit(sorted(items, reverse=True), capacity)\n",
        "\n",
        "def best_fit_decreasing(items, capacity=1.0):\n",
        "    sorted_items = sorted(items, reverse=True)\n",
        "    bins = []\n",
        "    bin_contents = []\n",
        "    for item in sorted_items:\n",
        "        best_idx = -1\n",
        "        best_space = float('inf')\n",
        "        for i, space in enumerate(bins):\n",
        "            if space >= item and space - item < best_space:\n",
        "                best_space = space - item\n",
        "                best_idx = i\n",
        "        if best_idx >= 0:\n",
        "            bins[best_idx] -= item\n",
        "            bin_contents[best_idx].append(item)\n",
        "        else:\n",
        "            bins.append(capacity - item)\n",
        "            bin_contents.append([item])\n",
        "    return bin_contents\n",
        "\n",
        "def display_bins(label, bins):\n",
        "    print(f'\\n{label}: {len(bins)} bins')\n",
        "    for i, b in enumerate(bins, 1):\n",
        "        used = sum(b)\n",
        "        bar = '#' * int(used * 20)\n",
        "        print(f'  Bin {i}: {[round(x,1) for x in b]} | Used: {used:.1f} '\",\"\n",
        "              f'[{bar:<20}]')\n",
        "\n",
        "items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]\n",
        "capacity = 1.0\n",
        "lower_bound = -(-sum(items) // capacity)  # Ceiling division\n",
        "\n",
        "print(f'Items: {items}')\n",
        "print(f'Capacity: {capacity}')\n",
        "print(f'Sum of items: {sum(items)}')\n",
        "print(f'Lower bound on bins: {int(lower_bound)}')\n",
        "\n",
        "ff_bins  = first_fit(items)\n",
        "ffd_bins = first_fit_decreasing(items)\n",
        "bfd_bins = best_fit_decreasing(items)\n",
        "\n",
        "\n",
        "\n",
        "display_bins('First Fit (FF)',           ff_bins)\n",
        "display_bins('First Fit Decreasing (FFD)', ffd_bins)\n",
        "display_bins('Best Fit Decreasing (BFD)', bfd_bins)\n",
        "\n",
        "print('f'\\nSummary: Lower Bound={int(lower_bound)}, FF={len(ff_bins)},\n",
        "FFD={len(ffd_bins)}, BFD={len(bfd_bins)}')"
      ]
    }
  ]
}