# Конвертація одиниць: Напишіть статичний метод для конвертації одиниць
# (наприклад, метричних до імперських або навпаки).
class UnitConverter:
    @staticmethod
    def meters_to_yards(meters):
        return meters * 1.09361

    @staticmethod
    def yards_to_meters(yards):
        return yards / 1.09361


yards = UnitConverter.meters_to_yards(10)
meters = UnitConverter.yards_to_meters(10)

print(f'10 метрів у ярдах = {yards}')
print(f'10 ярдів у метрах = {meters}')
