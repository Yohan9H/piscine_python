def ft_tqdm(lst: range) -> None:
    for i, elem in enumerate(lst):
        progress = int(i) + 1
        total = int(len(lst))
        percent = int((progress / total) * 100)
        bar_length = 98
        progress_length = int(bar_length * progress // total)

        bar = "█" * progress_length
        bar = bar.ljust(bar_length, "=")

        print(f"\r{percent}%|{bar}| {progress}/{total}", end="", flush=True)
        yield elem


if __name__ == "__main__":
    ft_tqdm()
