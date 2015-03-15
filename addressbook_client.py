
__author__ = 'Eric Chen'



import addressbook_pb2

TIMEOUT_SECONDS = 10


def format_information(contact):

    str = raw_input('Please input persion information, use ";" to split them:')

    if str.count(';') < 5:
        print "Input error!"

    tmp = str.split(';')

    contact.id = int(tmp[0])
    contact.name = tmp[1]
    contact.email = tmp[2]
    i = 3
    num = str.count(';')-3

    while num > 0 :

        phone_number = contact.phone.add()

        if tmp[i] == "mobile":
            phone_number.type = addressbook_pb2.Person.MOBILE
        elif tmp[i] == "home":
            phone_number.type = addressbook_pb2.Person.HOME
        elif tmp[i] == "work":
            phone_number.type = addressbook_pb2.Person.WORK

        phone_number.number = tmp[i+1]
        i=i+2
        num=num-2

    return contact


def print_contact(contact):
    print "ID: %d, Name: " % contact.id, contact.name
    if contact.email is not None:
        print "Email: ", contact.email
    phone_number_count = 0
    for phone_number in contact.phone:
        phone_number_count += 1
        print "Phone ", phone_number_count
        print "Type ", phone_number.type
        print "Number ", phone_number.number


def Insert_address(server_stub):
    contact = addressbook_pb2.Person()
    contact = format_information(contact)

    response = server_stub.InsertAddress(contact, TIMEOUT_SECONDS)
    print response.message


def lookup_addresses(server_stub):

    lookup_string = raw_input("Enter name of contact to find:\n")
    if lookup_string == "":
        print "name shouldn't be blank"
        return

    request = addressbook_pb2.Request(message=lookup_string)

    response = server_stub.LookUpAddresses(request, TIMEOUT_SECONDS)

    for contact in response.results:
        print_contact(contact)


def display_all_addresses(server_stub):
    all_request = addressbook_pb2.Request(message='')
    response = server_stub.DisplayAddresses(all_request, TIMEOUT_SECONDS)

    print "returned all addresses"
    for contact in response.contacts:
        print_contact(contact)


def run():
    with addressbook_pb2.early_adopter_create_AddressBookService_stub('localhost', 50055) as stub:
        while True:

            print "1 Insert address"
            print "2 Look up"
            print "3 Display addresses"
            print "4 Exit"

            selection = int(raw_input("Please select an option:"))
            if selection == 1:
                Insert_address(stub)
            elif selection == 2:
                lookup_addresses(stub)
            elif selection == 3:
                display_all_addresses(stub)
            elif selection == 4:
                print "Exit!"
                exit(9)
            else:
                print 'Choose a number above please!'


if __name__ == '__main__':
    run()