# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addressbook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='addressbook.proto',
  package='',
  serialized_pb=_b('\n\x11\x61\x64\x64ressbook.proto\"\xc8\x01\n\x06Person\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\"\n\x05phone\x18\x04 \x03(\x0b\x32\x13.Person.PhoneNumber\x1a\x44\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x02(\t\x12%\n\x04type\x18\x02 \x01(\x0e\x32\x11.Person.PhoneType:\x04HOME\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"(\n\x0b\x41\x64\x64ressBook\x12\x19\n\x08\x63ontacts\x18\x01 \x03(\x0b\x32\x07.Person\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1a\n\x07Request\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x06Result\x12\x18\n\x07results\x18\x01 \x03(\x0b\x32\x07.Person2\x91\x01\n\x12\x41\x64\x64ressBookService\x12%\n\rInsertAddress\x12\x07.Person\x1a\t.Response\"\x00\x12,\n\x10\x44isplayAddresses\x12\x08.Request\x1a\x0c.AddressBook\"\x00\x12&\n\x0fLookUpAddresses\x12\x08.Request\x1a\x07.Result\"\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PERSON_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='Person.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=179,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_PERSON_PHONETYPE)


_PERSON_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='Person.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Person.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Person.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=177,
)

_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Person.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Person.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone', full_name='Person.phone', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_PHONENUMBER, ],
  enum_types=[
    _PERSON_PHONETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=222,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contacts', full_name='AddressBook.contacts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=264,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=293,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Request.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=321,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='Result.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=357,
)

_PERSON_PHONENUMBER.fields_by_name['type'].enum_type = _PERSON_PHONETYPE
_PERSON_PHONENUMBER.containing_type = _PERSON
_PERSON.fields_by_name['phone'].message_type = _PERSON_PHONENUMBER
_PERSON_PHONETYPE.containing_type = _PERSON
_ADDRESSBOOK.fields_by_name['contacts'].message_type = _PERSON
_RESULT.fields_by_name['results'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(

  PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
    DESCRIPTOR = _PERSON_PHONENUMBER,
    __module__ = 'addressbook_pb2'
    # @@protoc_insertion_point(class_scope:Person.PhoneNumber)
    ))
  ,
  DESCRIPTOR = _PERSON,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  ))
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.PhoneNumber)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSBOOK,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:AddressBook)
  ))
_sym_db.RegisterMessage(AddressBook)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  ))
_sym_db.RegisterMessage(Result)


import abc
from grpc.early_adopter import implementations
from grpc.early_adopter import utilities
class EarlyAdopterAddressBookServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def InsertAddress(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DisplayAddresses(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def LookUpAddresses(self, request, context):
    raise NotImplementedError()
class EarlyAdopterAddressBookServiceServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterAddressBookServiceStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def InsertAddress(self, request):
    raise NotImplementedError()
  InsertAddress.async = None
  @abc.abstractmethod
  def DisplayAddresses(self, request):
    raise NotImplementedError()
  DisplayAddresses.async = None
  @abc.abstractmethod
  def LookUpAddresses(self, request):
    raise NotImplementedError()
  LookUpAddresses.async = None
def early_adopter_create_AddressBookService_server(servicer, port, root_certificates, key_chain_pairs):
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  method_service_descriptions = {
    "DisplayAddresses": utilities.unary_unary_service_description(
      servicer.DisplayAddresses,
      addressbook_pb2.Request.FromString,
      addressbook_pb2.AddressBook.SerializeToString,
    ),
    "InsertAddress": utilities.unary_unary_service_description(
      servicer.InsertAddress,
      addressbook_pb2.Person.FromString,
      addressbook_pb2.Response.SerializeToString,
    ),
    "LookUpAddresses": utilities.unary_unary_service_description(
      servicer.LookUpAddresses,
      addressbook_pb2.Request.FromString,
      addressbook_pb2.Result.SerializeToString,
    ),
  }
  return implementations.secure_server(method_service_descriptions, port, root_certificates, key_chain_pairs)
def early_adopter_create_AddressBookService_stub(host, port):
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  import addressbook_pb2
  method_invocation_descriptions = {
    "DisplayAddresses": utilities.unary_unary_invocation_description(
      addressbook_pb2.Request.SerializeToString,
      addressbook_pb2.AddressBook.FromString,
    ),
    "InsertAddress": utilities.unary_unary_invocation_description(
      addressbook_pb2.Person.SerializeToString,
      addressbook_pb2.Response.FromString,
    ),
    "LookUpAddresses": utilities.unary_unary_invocation_description(
      addressbook_pb2.Request.SerializeToString,
      addressbook_pb2.Result.FromString,
    ),
  }
  return implementations.insecure_stub(method_invocation_descriptions, host, port)
# @@protoc_insertion_point(module_scope)
