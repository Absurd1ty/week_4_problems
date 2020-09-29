"""You are given the array paths, where paths[i] = [cityAi, cityBi] 
means there exists a direct path going from cityAi to 
cityBi. Return the destination city, 
that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, 
there will be exactly 
one destination city.

 """
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        source_cities = []
        destination_cities = []
        
        for source, destination in paths:
            source_cities.append(source)
            destination_cities.append(destination)
        
        for destination in destination_cities :
            
            if destination not in source_cities:
                return destination