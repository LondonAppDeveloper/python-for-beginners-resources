class TempMixin:
    """Convert temperatures from metric to imperial (and reverse)."""

    def f_to_c(self, f):
        """Convert imperial to metric."""
        return (f - 32) / 1.8

    def c_to_f(self, c):
        """Convert metric to imperial."""
        return (c * 1.8) + 32


class DistanceMixin:
    """Convert distances from metric to imperial (and reverse)."""

    def m_to_km(self, miles):
        """Convert miles to km."""
        return miles * 1.60934

    def km_to_m(self, km):
        """Convert km to miles."""
        return km * 0.6213712


class DigitalStorageMixin:
    """Convert digital storage values."""

    def gb_to_mb(self, gb):
        """Convert gb to mb."""
        return gb * 1000

    def mb_to_gb(self, mb):
        """Convert mb to gb."""
        return mb / 1000


class Weather(TempMixin, DistanceMixin):
    """Details about the weather."""

    def __init__(self, celsius, kmph):
        """Initialise data."""
        self._celsius = celsius
        self._kmph = kmph

    def display(self, metric=True):
        """Display weather values."""
        if metric:
            temp = self._celsius
            wind = self._kmph
        else:
            temp = self.c_to_f(self._celsius)
            wind = self.km_to_m(self._kmph)
        
        print(f'Temp: {temp}, Wind Speed: {wind}.')
        print('--- END OF WEATHER ---')


london = Weather(12, 7)
london.display()
london.display(metric=False)


class HardDrive(TempMixin, DigitalStorageMixin):
    """Computer hard drive."""

    def __init__(self, space, celsius):
        """Initialise drive status."""
        self._space = space
        self._celsius = celsius

    def status(self, metric=True):
        """Display drive status."""
        if metric:
            temp = self._celsius
        else:
            temp = self.c_to_f(self._celsius)

        space = self.mb_to_gb(self._space)
        print(f'Space: {space}gb, Temp: {temp}.')
        print('--- END OF HARD DRIVE STATUS ---')


hd = HardDrive(800000, 22)
hd.status()
hd.status(metric=False)