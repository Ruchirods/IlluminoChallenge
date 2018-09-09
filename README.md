Steps to run the code:

1. from Illumino import Firewall
2. f1=Firewall(filePath)
3. f1.accept_packet("outbound","udp",1005,"52.12.48.00")

My code will rad the rule file in chuncks and if you find the match in a particular chunk the remaining data wont be checked for.
Also my code first checks if it has Direction and protocol match if not it wont progress on checking the others.
The final result with will either "True" or "False"