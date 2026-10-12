def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return length * width

if __name__ == "__main__":
    # Example usage
    try:
        length = 5
        width = 10
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    except ValueError as e:
        print(f"Error: {e}") 