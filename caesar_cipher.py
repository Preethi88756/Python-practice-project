alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

 
def caesar(original_text,shiftamount,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
        shiftamount*=-1                #3+(5*-1)

    for letter in original_text:

        if letter not in alphabet:
            output_text+=letter
        else:

            

            shifted_position=alphabet.index(letter)+shiftamount
            shifted_position%=len(alphabet)#0-25
            output_text+=alphabet[shifted_position]

    print(f"here is the {encode_or_decode}d result:{output_text}")



should_contain=True

while should_contain:
    direction=input("type 'encode'to encrypt and 'decode' to decrypt:\n").lower()
    text=input("type your message\n").lower()
    shift=int(input("type a shift number\n"))

    caesar(original_text=text,shiftamount=shift,encode_or_decode=direction)

    restart=input("type 'yes'if you want to continue. otherwize type'no'.\n").lower()
    if restart =="no":
        should_contain=False
        print("goodbye")
    




