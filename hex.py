def hex_to_dec(hex_str):
    """Convert a hexadecimal string to a decimal number."""
    return int(hex_str, 16)


def expand_ipv6(ipv6):
    """Expand an abbreviated IPv6 address to its full form."""
    if '::' in ipv6:
        # Split the address on the '::'
        left, right = ipv6.split('::')
        left_blocks = left.split(':') if left else []
        right_blocks = right.split(':') if right else []
        # Calculate how many blocks of zeros we need to insert
        num_zeros = 8 - (len(left_blocks) + len(right_blocks))
        # Insert the zeros
        zeros = ['0000'] * num_zeros
        full_blocks = left_blocks + zeros + right_blocks
    else:
        full_blocks = ipv6.split(':')

    # Ensure all blocks are 4 hex digits
    full_blocks = [block.zfill(4) for block in full_blocks]
    return full_blocks


def ipv6_to_decimal(ipv6):
    """Convert an IPv6 address to its decimal representation."""
    full_blocks = expand_ipv6(ipv6)
    decimal_blocks = [str(hex_to_dec(block)) for block in full_blocks]
    return ':'.join(decimal_blocks)


# Example usage
ipv6_address = input("IPv6: ")
decimal_representation = ipv6_to_decimal(ipv6_address)

print(f"Decimal Representation: {decimal_representation}")
