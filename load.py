from config import dataloader
def load_data(offline, url):
    try:
        df = dataloader.load_data(url)
    except Exception as e:
        print(f"[red]Failed to load data from URL: {e}")
        print(f"[yellow]Loading data from local file: {offline}")
        try:
            df = dataloader.load_data(offline)
        except Exception as e:
            print(f"[red]Failed to load data from local file: {e}")
            exit()
    return df
