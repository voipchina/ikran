# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='cert_logger.proto',
  package='chrome_browser_net',
  serialized_pb='\n\x11\x63\x65rt_logger.proto\x12\x12\x63hrome_browser_net\"L\n\x11\x43\x65rtLoggerRequest\x12\x10\n\x08hostname\x18\x01 \x02(\t\x12\x12\n\ncert_chain\x18\x02 \x02(\t\x12\x11\n\ttime_usec\x18\x03 \x02(\x03\"\xea\x01\n\x12\x43\x65rtLoggerResponse\x12\x45\n\x08response\x18\x01 \x02(\x0e\x32\x33.chrome_browser_net.CertLoggerResponse.ResponseCode\"\x8c\x01\n\x0cResponseCode\x12\x06\n\x02OK\x10\x01\x12\x17\n\x13MALFORMED_CERT_DATA\x10\x02\x12\x18\n\x14HOST_CERT_DONT_MATCH\x10\x03\x12\x17\n\x13ROOT_NOT_RECOGNIZED\x10\x04\x12\x17\n\x13ROOT_NOT_UNEXPECTED\x10\x05\x12\x0f\n\x0bOTHER_ERROR\x10\x06\x42\x02H\x03')



_CERTLOGGERRESPONSE_RESPONSECODE = descriptor.EnumDescriptor(
  name='ResponseCode',
  full_name='chrome_browser_net.CertLoggerResponse.ResponseCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='OK', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MALFORMED_CERT_DATA', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='HOST_CERT_DONT_MATCH', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROOT_NOT_RECOGNIZED', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROOT_NOT_UNEXPECTED', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='OTHER_ERROR', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=214,
  serialized_end=354,
)


_CERTLOGGERREQUEST = descriptor.Descriptor(
  name='CertLoggerRequest',
  full_name='chrome_browser_net.CertLoggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hostname', full_name='chrome_browser_net.CertLoggerRequest.hostname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cert_chain', full_name='chrome_browser_net.CertLoggerRequest.cert_chain', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_usec', full_name='chrome_browser_net.CertLoggerRequest.time_usec', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=41,
  serialized_end=117,
)


_CERTLOGGERRESPONSE = descriptor.Descriptor(
  name='CertLoggerResponse',
  full_name='chrome_browser_net.CertLoggerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='response', full_name='chrome_browser_net.CertLoggerResponse.response', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CERTLOGGERRESPONSE_RESPONSECODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=120,
  serialized_end=354,
)

_CERTLOGGERRESPONSE.fields_by_name['response'].enum_type = _CERTLOGGERRESPONSE_RESPONSECODE
_CERTLOGGERRESPONSE_RESPONSECODE.containing_type = _CERTLOGGERRESPONSE;
DESCRIPTOR.message_types_by_name['CertLoggerRequest'] = _CERTLOGGERREQUEST
DESCRIPTOR.message_types_by_name['CertLoggerResponse'] = _CERTLOGGERRESPONSE

class CertLoggerRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CERTLOGGERREQUEST
  
  # @@protoc_insertion_point(class_scope:chrome_browser_net.CertLoggerRequest)

class CertLoggerResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CERTLOGGERRESPONSE
  
  # @@protoc_insertion_point(class_scope:chrome_browser_net.CertLoggerResponse)

# @@protoc_insertion_point(module_scope)