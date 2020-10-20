# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ifaceinfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ifaceinfo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fifaceinfo.proto\"\x19\n\tOneDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1c\n\x0cServalDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\"F\n\x07\x41\x64\x64ress\x12\x12\n\niface_name\x18\x01 \x01(\t\x12\x0c\n\x04ipv6\x18\x02 \x01(\t\x12\x0c\n\x04mask\x18\x03 \x01(\t\x12\x0b\n\x03mac\x18\x04 \x01(\t2\\\n\tIfaceInfo\x12$\n\nGetOneInfo\x12\n.OneDevice\x1a\x08.Address\"\x00\x12)\n\nGetAllInfo\x12\r.ServalDevice\x1a\x08.Address\"\x00\x30\x01\x62\x06proto3'
)




_ONEDEVICE = _descriptor.Descriptor(
  name='OneDevice',
  full_name='OneDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='OneDevice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=44,
)


_SERVALDEVICE = _descriptor.Descriptor(
  name='ServalDevice',
  full_name='ServalDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ServalDevice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=74,
)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='iface_name', full_name='Address.iface_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ipv6', full_name='Address.ipv6', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask', full_name='Address.mask', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mac', full_name='Address.mac', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['OneDevice'] = _ONEDEVICE
DESCRIPTOR.message_types_by_name['ServalDevice'] = _SERVALDEVICE
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OneDevice = _reflection.GeneratedProtocolMessageType('OneDevice', (_message.Message,), {
  'DESCRIPTOR' : _ONEDEVICE,
  '__module__' : 'ifaceinfo_pb2'
  # @@protoc_insertion_point(class_scope:OneDevice)
  })
_sym_db.RegisterMessage(OneDevice)

ServalDevice = _reflection.GeneratedProtocolMessageType('ServalDevice', (_message.Message,), {
  'DESCRIPTOR' : _SERVALDEVICE,
  '__module__' : 'ifaceinfo_pb2'
  # @@protoc_insertion_point(class_scope:ServalDevice)
  })
_sym_db.RegisterMessage(ServalDevice)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'ifaceinfo_pb2'
  # @@protoc_insertion_point(class_scope:Address)
  })
_sym_db.RegisterMessage(Address)



_IFACEINFO = _descriptor.ServiceDescriptor(
  name='IfaceInfo',
  full_name='IfaceInfo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=148,
  serialized_end=240,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOneInfo',
    full_name='IfaceInfo.GetOneInfo',
    index=0,
    containing_service=None,
    input_type=_ONEDEVICE,
    output_type=_ADDRESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllInfo',
    full_name='IfaceInfo.GetAllInfo',
    index=1,
    containing_service=None,
    input_type=_SERVALDEVICE,
    output_type=_ADDRESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IFACEINFO)

DESCRIPTOR.services_by_name['IfaceInfo'] = _IFACEINFO

# @@protoc_insertion_point(module_scope)
