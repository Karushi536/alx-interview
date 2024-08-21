#!/usr/bin/python3

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0

    for byte in data:
        # Check if the byte is in the valid range
        if byte < 0 or byte > 255:
            return False

        # Determine the number of leading 1's in the byte
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                num_bytes = 0  # 1-byte character
            elif byte >> 5 == 0b110:
                num_bytes = 1  # 2-byte character
            elif byte >> 4 == 0b1110:
                num_bytes = 2  # 3-byte character
            elif byte >> 3 == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid start byte
        else:
            # Byte should start with 10xxxxxx
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # There should be no pending bytes
    return num_bytes == 0
