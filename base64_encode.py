import sys 
# Take a string
if len(sys.argv)>2:
    print("Multiple inputs are not supported kindly pass the argument inside quotes.\nUsage: python %s 'input' or 'inpu t' or 'inp ut'"% sys.argv[0])
    sys.exit(1)
if len(sys.argv) != 2:
    raw_data = input("Enter the string to convert to base64: ")
else:
    raw_data = sys.argv[1]

# First we need to split all the characters from the string 
data = list(raw_data)
# Second we need to get binary data for each character
bin_data = []

for _ in data:
    if _ == " ":
        bin_data.append("00100000")
    else:
        bin_data.append("0"+bin(ord(_))[2:]) # Now we have binary data from the string

# Third we need to concatinate all the binary values together
glued_bin = ""
for _ in bin_data:
    glued_bin += _ # Bro i got zero idea how i got it to work in first try T-T xD.

# Fourth we need to divide whole string into 6 pairs
six_bin = []

temp = ""
for _ in glued_bin:
    temp += _
    if len(temp) == 6:
        six_bin.append(temp)
        temp = "" # spent almost 5 hours to figure such small thing
if len(temp) < 6 and len(temp) > 0:
    i = 6 - len(temp)
    for j in range(i):
        temp += '0'
    six_bin.append(temp)

# Fifth we need to make it 8 pair with 00 in front 
eight_bin = []
for _ in six_bin:
    eight_bin.append("00"+_)

# Sixth we need to convert each group from binary to decimal
bin_to_dec = []
for _ in eight_bin:
    bin_to_dec.append(int(str(_),2))

# Seventh we need to convert base64 indices to base64 character from base64 character table
bs_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

f_str = ""
for i in bin_to_dec:
    f_str+=bs_char[i]
print(f"Input: {raw_data}\nBase64 String: {f_str}")
