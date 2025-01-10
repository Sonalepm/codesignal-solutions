def solution(input_string):
    filtered_chars = [char.lower() for char in input_string if char.isalnum()]
    start = 0
    end = len(filtered_chars) -1
    while start< end:
        if filtered_chars[start] != filtered_chars[end]:
            return False
        start += 1
        end -= 1
    return True
            
        
    
