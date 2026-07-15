from app.config.loader import ConfigLoader

settings = ConfigLoader.load()

print(settings.scoring.price.cheap)
print(settings.scanner.refresh_seconds)
print(settings.reports.output_folder)