import socket

# Step 2: Send 0800 message with bit 70 set to 301
def send_0800_message(ip_address, port):
    message = b'0800' + b'301'  # Construct message
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        s.sendall(message)
        response = s.recv(1024)
        return response

# Step 3: Parse header and trailer from 0810 response
def parse_header_trailer(response):
    header = response[:10]
    trailer = response[-10:]
    return header, trailer

# Step 4: Resend message with correct header and trailer
def resend_message(header, trailer):
    message = b'0800' + b'301'  # Construct message
    full_message = header + message + trailer
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        s.sendall(full_message)
        response = s.recv(1024)
        return response

# Step 5: Confirm 0810 response
def confirm_response(response):
    # Disregarding bit 39
    response_without_bit_39 = response.replace(b'39', b'')
    return response_without_bit_39
