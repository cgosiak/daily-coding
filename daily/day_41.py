"""
Given an unordered list of flights taken by someone, each represented as 
(origin, destination) pairs, and a starting airport, compute the person's 
itinerary. If no such itinerary exists, return null. If there are multiple 
possible itineraries, return the lexicographically smallest one. All flights 
must be used in the itinerary.

For example, given the list of flights 
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', 
you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] 
and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] 
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. 
However, the first one is lexicographically smaller.
"""
from typing import List, Tuple, Dict
import unittest


class Airport(object):

    def __init__(self, name: str):
        self.name: str = name
        self.outbound_flights: List = []

    def add_outbound_flight(self, airport):
        self.outbound_flights.append(airport)

    def get_itenerary(self) -> List[str]:
        itenerary: List[str] = [self.name]
        for outbound_flight in self.outbound_flights:
            itenerary.extend(outbound_flight.get_itenerary())
        return itenerary


class FlightSchedule(object):

    def __init__(self, flights: List[Tuple]):
        self.flights: List[Tuple] = flights
        self.airports: Dict[str, Airport] = {}
        for airport_a, airport_b in flights:
            if airport_a not in self.airports:
                self.airports[airport_a] = Airport(airport_a)
            if airport_b not in self.airports:
                self.airports[airport_b] = Airport(airport_b)
            
            self.airports[airport_a].add_outbound_flight(self.airports[airport_b])

    def get_itenerary(self, starting_airport: str) -> List[str]:
        itenerary: List[str] = self.airports[starting_airport].get_itenerary()
        return itenerary if not set(self.airports.keys()).difference(set(itenerary)) else None



class TestItenerary(unittest.TestCase):

    def test_1(self):
        flightSchedule: FlightSchedule = FlightSchedule([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')])
        self.assertEqual(flightSchedule.get_itenerary('YUL'), ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'])

    def test_2(self):
        flightSchedule: FlightSchedule = FlightSchedule([('SFO', 'COM'), ('COM', 'YYZ')])
        self.assertEqual(flightSchedule.get_itenerary('COM'), None)


unittest.main()
