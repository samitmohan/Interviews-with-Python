class Solution():
    # Solution class carries method for printing itinerary
    def __init__(self):
        pass

    def printItinerary(self,d):
        # First step : create a reversed mapping. Here also for storing key value pairs dictionary is used.
        reverse_d = dict()
        for i in d:
            reverse_d[d[i]] = i
        # Second step : find the starting point. Starting point will be that value which is not present in 'd' as key.
        for i in reverse_d:
            if reverse_d[i] not in reverse_d:
                starting_pt = reverse_d[i]
                break;
        #Third step : simply proceed one by one to print whole route. Assuming that there exist Starting point.
        while(starting_pt in d):
            print(starting_pt,"->",d[starting_pt],end=", ")
            starting_pt = d[starting_pt]
 
if __name__=="__main__":
    d = dict()
    d["Chennai"] = "Banglore"
    d["Bombay"] = "Delhi"
    d["Goa"] = "Chennai"
    d["Delhi"] = "Goa"
 
    # call for method that would print itinerary.
    obj = Solution()
    obj.printItinerary(d)