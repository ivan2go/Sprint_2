class PointsForPlace:
    def __init__(self):
        self.place = 0
    
    def get_points_for_place(self, place):
        if place > 100:
            return f'Баллы начисляются только первым 100 участникам'
        
        elif place < 1:
            return f'Спортсмен не может занять нулевое или отрицательное место'
        
        else:
            place = 101 - place
            return f'Спортсмен занимает {place} место'


class PointsForMeters:
    def __init__(self):
        self.points = 0
        self.meters = 0
    
    def get_points_for_meters(self, meters):
        if meters < 0:
            return f'Количество метров не может быть отрицательным'
        
        else:
            points = meters * 0.5
            return f'Спортсмен получил {points} очков'

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()
        
    def get_points_for_meters(self, meters):
        return super().get_points_for_meters(meters)
    
    def get_points_for_place(self, place):
        return super().get_points_for_place(place)
    
    def get_total_points(self, meters, place):
        total = meters + place
        return f'Спортсмен получил {total} очков всего'




points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 