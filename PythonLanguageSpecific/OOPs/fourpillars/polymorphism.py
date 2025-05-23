"""
Polymorphism allows objects of different types to be treated as instances of the same type through a common interface,
enabling the same operation to behave differently on different classes.

Types of Polymorphism:
    Method Overriding: Same method name, different implementations
    Duck Typing: "If it looks like a duck and quacks like a duck, it's a duck"
    Operator Overloading: Customizing behavior of operators
"""

import math
from abc import ABC, abstractmethod


# base
class Shape(ABC):
    def __init__(self, color: str = "white") -> None:
        self.color = color

    @abstractmethod
    def calculate_area(self) -> float:
        """Abstract method - must be implemented by subclasses."""
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Abstract method - must be implemented by subclasses."""
        pass

    def get_info(self) -> str:
        return f"{self.__class__.__name__} (Color : {self.color})"

    def draw(self) -> str:
        return f"Drawing a {self.color} {self.__class__.__name__.lower()}"


class Circle(Shape):
    def __init__(self, radius: float, color: str = "white") -> None:
        super().__init__(color)
        if radius <= 0:
            raise ValueError("Radius > 0")
        self.radius = radius

    # overriding
    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Radius: {self.radius}"

    # operator overloading
    def __eq__(self, other) -> bool:
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius and self.color == other.color

    def __str__(self) -> str:
        return f"Circle(r={self.radius}, color={self.color})"


class Rectangle(Shape):
    """Rectangle implementation of Shape."""

    def __init__(self, width: float, height: float, color: str = "white"):
        super().__init__(color)
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_info(self) -> str:
        """Override to include dimensions."""
        base_info = super().get_info()
        return f"{base_info}, Dimensions: {self.width}x{self.height}"

    def is_square(self) -> bool:
        """Rectangle-specific method."""
        return self.width == self.height

    # Operator overloading
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return (
            self.width == other.width
            and self.height == other.height
            and self.color == other.color
        )

    def __add__(self, other):
        """Add two rectangles by combining their areas."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        # Create a new rectangle with combined area (keeping proportions)
        new_area = self.calculate_area() + other.calculate_area()
        new_width = math.sqrt(new_area)
        new_height = new_width
        return Rectangle(new_width, new_height, self.color)

    def __str__(self) -> str:
        return f"Rectangle({self.width}x{self.height}, color={self.color})"


class Triangle(Shape):
    """Triangle implementation of Shape."""

    def __init__(
        self, side_a: float, side_b: float, side_c: float, color: str = "white"
    ):
        super().__init__(color)
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides must be positive")
        if not self._is_valid_triangle(side_a, side_b, side_c):
            raise ValueError(
                "Invalid triangle: sides don't satisfy triangle inequality"
            )

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        """Check if three sides can form a valid triangle."""
        return (a + b > c) and (a + c > b) and (b + c > a)

    def calculate_area(self) -> float:
        """Triangle area using Heron's formula."""
        s = self.calculate_perimeter() / 2  # Semi-perimeter
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def calculate_perimeter(self) -> float:
        """Triangle perimeter calculation."""
        return self.side_a + self.side_b + self.side_c

    def get_info(self) -> str:
        """Override to include side information."""
        base_info = super().get_info()
        return f"{base_info}, Sides: {self.side_a}, {self.side_b}, {self.side_c}"

    def get_triangle_type(self) -> str:
        """Determine triangle type."""
        sides = sorted([self.side_a, self.side_b, self.side_c])
        if sides[0] == sides[2]:  # All sides equal
            return "Equilateral"
        elif sides[0] == sides[1] or sides[1] == sides[2]:  # Two sides equal
            return "Isosceles"
        else:
            return "Scalene"

    def __str__(self) -> str:
        return f"Triangle({self.side_a}, {self.side_b}, {self.side_c}, color = {self.color})"


# polymorphic functions that work with any shape
def print_shape_details(shape) -> None:
    """Polymorphic function - works with any object that has the required methods."""
    print(f"Shape: {shape.get_info()}")
    print(f"Area: {shape.calculate_area():.2f}")
    print(f"Perimeter: {shape.calculate_perimeter():.2f}")
    print(f"Drawing: {shape.draw()}")
    print("-" * 40)


def compare_areas(shapes: list) -> None:
    """Compare areas of different shapes polymorphically."""
    print("Area Comparison:")
    sorted_shapes = sorted(shapes, key=lambda s: s.calculate_area(), reverse=True)

    for i, shape in enumerate(sorted_shapes, 1):
        print(f"{i}. {shape.__class__.__name__}: {shape.calculate_area():.2f}")


def total_area(shapes: list) -> float:
    """Calculate total area of all shapes."""
    return sum(shape.calculate_area() for shape in shapes)


# Demonstration of operator overloading
class Vector:
    """Vector class demonstrating operator overloading."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Override + operator."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Override - operator."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        """Override * operator for scalar multiplication."""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        """Right multiplication (scalar * vector)."""
        return self.__mul__(scalar)

    def __eq__(self, other):
        """Override == operator."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def magnitude(self) -> float:
        """Calculate vector magnitude."""
        return math.sqrt(self.x**2 + self.y**2)


# Usage example demonstrating polymorphism
if __name__ == "__main__":
    print("=== Polymorphism Demonstration ===\n")

    # Create different shape objects
    circle = Circle(5, "red")
    rectangle = Rectangle(4, 6, "blue")
    triangle = Triangle(3, 4, 5, "green")

    # Store in a list - polymorphic collection
    shapes = [circle, rectangle, triangle]

    print("1. Method Polymorphism - Same method, different implementations:")
    for shape in shapes:
        print_shape_details(shape)

    print("\n2. Polymorphic Operations:")
    compare_areas(shapes)
    print(f"\nTotal area of all shapes: {total_area(shapes):.2f}")

    print("\n3. Operator Overloading with Shapes:")
    circle1 = Circle(3, "red")
    circle2 = Circle(3, "red")
    circle3 = Circle(4, "red")

    print(f"circle1 == circle2: {circle1 == circle2}")  # True
    print(f"circle1 == circle3: {circle1 == circle3}")  # False

    rect1 = Rectangle(2, 3, "blue")
    rect2 = Rectangle(3, 4, "blue")
    rect3 = rect1 + rect2  # Adding rectangles
    print(f"Rectangle addition: {rect1} + {rect2} = {rect3}")

    print("\n4. Vector Operator Overloading:")
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v1 = {3 * v1}")
    print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
    print(f"Magnitude of v1: {v1.magnitude():.2f}")
