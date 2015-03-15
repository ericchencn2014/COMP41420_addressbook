__author__ = 'Eric Chen'



import time

import addressbook_pb2


DAY_IN_SECONDS = 60 * 60 * 24


class AddressBookService(addressbook_pb2.EarlyAdopterAddressBookServiceServicer):

    address_book = addressbook_pb2.AddressBook()

    def InsertAddress(self, request, context):
        self.address_book.contacts.extend([request])

        return addressbook_pb2.Response(message = 'Insert successlly')

    def DisplayAddresses(self, request, context):
        return addressbook_pb2.AddressBook(contacts=self.address_book.contacts)


    def LookUpAddresses(self, request, context):
        results = []

        for contact in self.address_book.contacts:
            if request.message in contact.name:
                results.append(contact)

        return addressbook_pb2.Result(results=results)



def serve():
    server = addressbook_pb2.early_adopter_create_AddressBookService_server(
        AddressBookService(), 50055, None, None)
    server.start()

    try:
        while True:
            time.sleep(DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
    serve()
