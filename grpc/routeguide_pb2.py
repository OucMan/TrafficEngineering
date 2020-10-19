# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routeguide.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='routeguide.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10routeguide.proto\",\n\x05Point\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\"3\n\tRectangle\x12\x12\n\x02lo\x18\x01 \x01(\x0b\x32\x06.Point\x12\x12\n\x02hi\x18\x02 \x01(\x0b\x32\x06.Point\"1\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x08location\x18\x02 \x01(\x0b\x32\x06.Point\"6\n\tRouteNote\x12\x18\n\x08location\x18\x01 \x01(\x0b\x32\x06.Point\x12\x0f\n\x07message\x18\x02 \x01(\t\"b\n\x0cRouteSummary\x12\x13\n\x0bpoint_count\x18\x01 \x01(\x05\x12\x15\n\rfeature_count\x18\x02 \x01(\x05\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\x14\n\x0c\x65lapsed_time\x18\x04 \x01(\x05\x32\xac\x01\n\nRouteGuide\x12 \n\nGetFeature\x12\x06.Point\x1a\x08.Feature\"\x00\x12\'\n\x0bListFeature\x12\n.Rectangle\x1a\x08.Feature\"\x00\x30\x01\x12(\n\x0bRecordRoute\x12\x06.Point\x1a\r.RouteSummary\"\x00(\x01\x12)\n\tRouteChat\x12\n.RouteNote\x1a\n.RouteNote\"\x00(\x01\x30\x01\x62\x06proto3')
)




_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Point.latitude', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Point.longitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=20,
  serialized_end=64,
)


_RECTANGLE = _descriptor.Descriptor(
  name='Rectangle',
  full_name='Rectangle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lo', full_name='Rectangle.lo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hi', full_name='Rectangle.hi', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=66,
  serialized_end=117,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Feature.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='Feature.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=119,
  serialized_end=168,
)


_ROUTENOTE = _descriptor.Descriptor(
  name='RouteNote',
  full_name='RouteNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='RouteNote.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='RouteNote.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=170,
  serialized_end=224,
)


_ROUTESUMMARY = _descriptor.Descriptor(
  name='RouteSummary',
  full_name='RouteSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point_count', full_name='RouteSummary.point_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_count', full_name='RouteSummary.feature_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='RouteSummary.distance', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elapsed_time', full_name='RouteSummary.elapsed_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=226,
  serialized_end=324,
)

_RECTANGLE.fields_by_name['lo'].message_type = _POINT
_RECTANGLE.fields_by_name['hi'].message_type = _POINT
_FEATURE.fields_by_name['location'].message_type = _POINT
_ROUTENOTE.fields_by_name['location'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Rectangle'] = _RECTANGLE
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['RouteNote'] = _ROUTENOTE
DESCRIPTOR.message_types_by_name['RouteSummary'] = _ROUTESUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'routeguide_pb2'
  # @@protoc_insertion_point(class_scope:Point)
  ))
_sym_db.RegisterMessage(Point)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), dict(
  DESCRIPTOR = _RECTANGLE,
  __module__ = 'routeguide_pb2'
  # @@protoc_insertion_point(class_scope:Rectangle)
  ))
_sym_db.RegisterMessage(Rectangle)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'routeguide_pb2'
  # @@protoc_insertion_point(class_scope:Feature)
  ))
_sym_db.RegisterMessage(Feature)

RouteNote = _reflection.GeneratedProtocolMessageType('RouteNote', (_message.Message,), dict(
  DESCRIPTOR = _ROUTENOTE,
  __module__ = 'routeguide_pb2'
  # @@protoc_insertion_point(class_scope:RouteNote)
  ))
_sym_db.RegisterMessage(RouteNote)

RouteSummary = _reflection.GeneratedProtocolMessageType('RouteSummary', (_message.Message,), dict(
  DESCRIPTOR = _ROUTESUMMARY,
  __module__ = 'routeguide_pb2'
  # @@protoc_insertion_point(class_scope:RouteSummary)
  ))
_sym_db.RegisterMessage(RouteSummary)



_ROUTEGUIDE = _descriptor.ServiceDescriptor(
  name='RouteGuide',
  full_name='RouteGuide',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=327,
  serialized_end=499,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeature',
    full_name='RouteGuide.GetFeature',
    index=0,
    containing_service=None,
    input_type=_POINT,
    output_type=_FEATURE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListFeature',
    full_name='RouteGuide.ListFeature',
    index=1,
    containing_service=None,
    input_type=_RECTANGLE,
    output_type=_FEATURE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RecordRoute',
    full_name='RouteGuide.RecordRoute',
    index=2,
    containing_service=None,
    input_type=_POINT,
    output_type=_ROUTESUMMARY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RouteChat',
    full_name='RouteGuide.RouteChat',
    index=3,
    containing_service=None,
    input_type=_ROUTENOTE,
    output_type=_ROUTENOTE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTEGUIDE)

DESCRIPTOR.services_by_name['RouteGuide'] = _ROUTEGUIDE

# @@protoc_insertion_point(module_scope)
