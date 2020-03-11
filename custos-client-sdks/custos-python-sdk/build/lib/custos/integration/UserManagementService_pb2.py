# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserManagementService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
import custos.core.UserProfileService_pb2 as UserProfileService__pb2
import custos.core.IamAdminService_pb2 as IamAdminService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='UserManagementService.proto',
  package='org.apache.custos.user.management.service',
  syntax='proto3',
  serialized_options=b'P\001',
  serialized_pb=b'\n\x1bUserManagementService.proto\x12)org.apache.custos.user.management.service\x1a\x1cgoogle/api/annotations.proto\x1a\x18UserProfileService.proto\x1a\x15IamAdminService.proto\"\xc3\x01\n\x12UserProfileRequest\x12I\n\x0cuser_profile\x18\x01 \x01(\x0b\x32\x33.org.apache.custos.user.profile.service.UserProfile\x12\x10\n\x08\x63lientId\x18\x02 \x01(\t\x12\x10\n\x08tenantId\x18\x03 \x01(\x03\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x04 \x01(\t\x12\x14\n\x0c\x63lientSecret\x18\x05 \x01(\t\x12\x13\n\x0bperformedBy\x18\x06 \x01(\t\"o\n\x0eGetUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12K\n\x11userSearchRequest\x18\x02 \x01(\x0b\x32\x30.org.apache.custos.iam.service.UserSearchRequest\"\xa1\x01\n\x0fGetUsersRequest\x12\x10\n\x08tenantId\x18\x01 \x01(\x03\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x0e\n\x06offset\x18\x04 \x01(\x05\x12\r\n\x05limit\x18\x05 \x01(\x05\x12\x0e\n\x06search\x18\x06 \x01(\t\x12\x13\n\x0biamClientId\x18\x07 \x01(\t\x12\x17\n\x0fiamClientSecret\x18\x08 \x01(\t\"\x88\x01\n\rResetPassword\x12\x10\n\x08tenantId\x18\x01 \x01(\x03\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x13\n\x0biamClientId\x18\x05 \x01(\t\x12\x17\n\x0fiamClientSecret\x18\x06 \x01(\t\"j\n\x14ResetPasswordRequest\x12R\n\x10passwordMetadata\x18\x01 \x01(\x0b\x32\x38.org.apache.custos.user.management.service.ResetPassword2\xef\x18\n\x15UserManagementService\x12\xa3\x01\n\x0cregisterUser\x12\x32.org.apache.custos.iam.service.RegisterUserRequest\x1a\x33.org.apache.custos.iam.service.RegisterUserResponse\"*\x82\xd3\xe4\x93\x02$\"\x1c/user-management/v1.0.0/user:\x04user\x12\xb1\x01\n\x16registerAndEnableUsers\x12\x33.org.apache.custos.iam.service.RegisterUsersRequest\x1a\x34.org.apache.custos.iam.service.RegisterUsersResponse\",\x82\xd3\xe4\x93\x02&\"\x1d/user-management/v1.0.0/users:\x05users\x12\xa8\x01\n\x11\x61\x64\x64UserAttributes\x12\x37.org.apache.custos.iam.service.AddUserAttributesRequest\x1a..org.apache.custos.iam.service.OperationStatus\"*\x82\xd3\xe4\x93\x02$\"\"/user-management/v1.0.0/attributes\x12\xad\x01\n\x14\x64\x65leteUserAttributes\x12\x39.org.apache.custos.iam.service.DeleteUserAttributeRequest\x1a..org.apache.custos.iam.service.OperationStatus\"*\x82\xd3\xe4\x93\x02$*\"/user-management/v1.0.0/attributes\x12\xa8\x01\n\nenableUser\x12\x30.org.apache.custos.iam.service.UserSearchRequest\x1a\x31.org.apache.custos.iam.service.UserRepresentation\"5\x82\xd3\xe4\x93\x02/\"\'/user-management/v1.0.0/user/activation:\x04user\x12\xa2\x01\n\x0f\x61\x64\x64RolesToUsers\x12\x32.org.apache.custos.iam.service.AddUserRolesRequest\x1a..org.apache.custos.iam.service.OperationStatus\"+\x82\xd3\xe4\x93\x02%\"#/user-management/v1.0.0/users/roles\x12\xaa\x01\n\risUserEnabled\x12\x30.org.apache.custos.iam.service.UserSearchRequest\x1a/.org.apache.custos.iam.service.CheckingResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./user-management/v1.0.0/user/activation/status\x12\xab\x01\n\x13isUsernameAvailable\x12\x30.org.apache.custos.iam.service.UserSearchRequest\x1a/.org.apache.custos.iam.service.CheckingResponse\"1\x82\xd3\xe4\x93\x02+\x12)/user-management/v1.0.0/user/availability\x12\x94\x01\n\x07getUser\x12\x30.org.apache.custos.iam.service.UserSearchRequest\x1a\x31.org.apache.custos.iam.service.UserRepresentation\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/user-management/v1.0.0/user\x12\x95\x01\n\tfindUsers\x12/.org.apache.custos.iam.service.FindUsersRequest\x1a\x30.org.apache.custos.iam.service.FindUsersResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/user-management/v1.0.0/users\x12\xa1\x01\n\rresetPassword\x12\x30.org.apache.custos.iam.service.ResetUserPassword\x1a/.org.apache.custos.iam.service.CheckingResponse\"-\x82\xd3\xe4\x93\x02\'\x1a%/user-management/v1.0.0/user/password\x12\x9b\x01\n\ndeleteUser\x12\x30.org.apache.custos.iam.service.UserSearchRequest\x1a/.org.apache.custos.iam.service.CheckingResponse\"*\x82\xd3\xe4\x93\x02$*\x1c/user-management/v1.0.0/user:\x04user\x12\xa5\x01\n\x0f\x64\x65leteUserRoles\x12\x35.org.apache.custos.iam.service.DeleteUserRolesRequest\x1a/.org.apache.custos.iam.service.CheckingResponse\"*\x82\xd3\xe4\x93\x02$*\"/user-management/v1.0.0/user/roles\x12\xc3\x01\n\x11updateUserProfile\x12=.org.apache.custos.user.management.service.UserProfileRequest\x1a\x33.org.apache.custos.user.profile.service.UserProfile\":\x82\xd3\xe4\x93\x02\x34\x1a$/user-management/v1.0.0/user/profile:\x0cuser_profile\x12\xb2\x01\n\x0egetUserProfile\x12=.org.apache.custos.user.management.service.UserProfileRequest\x1a\x33.org.apache.custos.user.profile.service.UserProfile\",\x82\xd3\xe4\x93\x02&\x12$/user-management/v1.0.0/user/profile\x12\xb5\x01\n\x11\x64\x65leteUserProfile\x12=.org.apache.custos.user.management.service.UserProfileRequest\x1a\x33.org.apache.custos.user.profile.service.UserProfile\",\x82\xd3\xe4\x93\x02&*$/user-management/v1.0.0/user/profile\x12\xce\x01\n\x1agetAllUserProfilesInTenant\x12=.org.apache.custos.user.management.service.UserProfileRequest\x1a\x42.org.apache.custos.user.profile.service.GetAllUserProfilesResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/user-management/v1.0.0/users/profile\x12\xd8\x01\n\x19getUserProfileAuditTrails\x12\x42.org.apache.custos.user.profile.service.GetUpdateAuditTrailRequest\x1a\x43.org.apache.custos.user.profile.service.GetUpdateAuditTrailResponse\"2\x82\xd3\xe4\x93\x02,\x12*/user-management/v1.0.0/user/profile/auditB\x02P\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,UserProfileService__pb2.DESCRIPTOR,IamAdminService__pb2.DESCRIPTOR,])




_USERPROFILEREQUEST = _descriptor.Descriptor(
  name='UserProfileRequest',
  full_name='org.apache.custos.user.management.service.UserProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_profile', full_name='org.apache.custos.user.management.service.UserProfileRequest.user_profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='org.apache.custos.user.management.service.UserProfileRequest.clientId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenantId', full_name='org.apache.custos.user.management.service.UserProfileRequest.tenantId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='org.apache.custos.user.management.service.UserProfileRequest.accessToken', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientSecret', full_name='org.apache.custos.user.management.service.UserProfileRequest.clientSecret', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='performedBy', full_name='org.apache.custos.user.management.service.UserProfileRequest.performedBy', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=154,
  serialized_end=349,
)


_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='org.apache.custos.user.management.service.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='org.apache.custos.user.management.service.GetUserRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userSearchRequest', full_name='org.apache.custos.user.management.service.GetUserRequest.userSearchRequest', index=1,
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
  serialized_start=351,
  serialized_end=462,
)


_GETUSERSREQUEST = _descriptor.Descriptor(
  name='GetUsersRequest',
  full_name='org.apache.custos.user.management.service.GetUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tenantId', full_name='org.apache.custos.user.management.service.GetUsersRequest.tenantId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='org.apache.custos.user.management.service.GetUsersRequest.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='org.apache.custos.user.management.service.GetUsersRequest.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='org.apache.custos.user.management.service.GetUsersRequest.offset', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='org.apache.custos.user.management.service.GetUsersRequest.limit', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search', full_name='org.apache.custos.user.management.service.GetUsersRequest.search', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iamClientId', full_name='org.apache.custos.user.management.service.GetUsersRequest.iamClientId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iamClientSecret', full_name='org.apache.custos.user.management.service.GetUsersRequest.iamClientSecret', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=465,
  serialized_end=626,
)


_RESETPASSWORD = _descriptor.Descriptor(
  name='ResetPassword',
  full_name='org.apache.custos.user.management.service.ResetPassword',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tenantId', full_name='org.apache.custos.user.management.service.ResetPassword.tenantId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='org.apache.custos.user.management.service.ResetPassword.accessToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='org.apache.custos.user.management.service.ResetPassword.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='org.apache.custos.user.management.service.ResetPassword.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iamClientId', full_name='org.apache.custos.user.management.service.ResetPassword.iamClientId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iamClientSecret', full_name='org.apache.custos.user.management.service.ResetPassword.iamClientSecret', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=629,
  serialized_end=765,
)


_RESETPASSWORDREQUEST = _descriptor.Descriptor(
  name='ResetPasswordRequest',
  full_name='org.apache.custos.user.management.service.ResetPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='passwordMetadata', full_name='org.apache.custos.user.management.service.ResetPasswordRequest.passwordMetadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=767,
  serialized_end=873,
)

_USERPROFILEREQUEST.fields_by_name['user_profile'].message_type = UserProfileService__pb2._USERPROFILE
_GETUSERREQUEST.fields_by_name['userSearchRequest'].message_type = IamAdminService__pb2._USERSEARCHREQUEST
_RESETPASSWORDREQUEST.fields_by_name['passwordMetadata'].message_type = _RESETPASSWORD
DESCRIPTOR.message_types_by_name['UserProfileRequest'] = _USERPROFILEREQUEST
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['GetUsersRequest'] = _GETUSERSREQUEST
DESCRIPTOR.message_types_by_name['ResetPassword'] = _RESETPASSWORD
DESCRIPTOR.message_types_by_name['ResetPasswordRequest'] = _RESETPASSWORDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserProfileRequest = _reflection.GeneratedProtocolMessageType('UserProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERPROFILEREQUEST,
  '__module__' : 'UserManagementService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.user.management.service.UserProfileRequest)
  })
_sym_db.RegisterMessage(UserProfileRequest)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'UserManagementService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.user.management.service.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUsersRequest = _reflection.GeneratedProtocolMessageType('GetUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERSREQUEST,
  '__module__' : 'UserManagementService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.user.management.service.GetUsersRequest)
  })
_sym_db.RegisterMessage(GetUsersRequest)

ResetPassword = _reflection.GeneratedProtocolMessageType('ResetPassword', (_message.Message,), {
  'DESCRIPTOR' : _RESETPASSWORD,
  '__module__' : 'UserManagementService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.user.management.service.ResetPassword)
  })
_sym_db.RegisterMessage(ResetPassword)

ResetPasswordRequest = _reflection.GeneratedProtocolMessageType('ResetPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETPASSWORDREQUEST,
  '__module__' : 'UserManagementService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.user.management.service.ResetPasswordRequest)
  })
_sym_db.RegisterMessage(ResetPasswordRequest)


DESCRIPTOR._options = None

_USERMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='UserManagementService',
  full_name='org.apache.custos.user.management.service.UserManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=876,
  serialized_end=4059,
  methods=[
  _descriptor.MethodDescriptor(
    name='registerUser',
    full_name='org.apache.custos.user.management.service.UserManagementService.registerUser',
    index=0,
    containing_service=None,
    input_type=IamAdminService__pb2._REGISTERUSERREQUEST,
    output_type=IamAdminService__pb2._REGISTERUSERRESPONSE,
    serialized_options=b'\202\323\344\223\002$\"\034/user-management/v1.0.0/user:\004user',
  ),
  _descriptor.MethodDescriptor(
    name='registerAndEnableUsers',
    full_name='org.apache.custos.user.management.service.UserManagementService.registerAndEnableUsers',
    index=1,
    containing_service=None,
    input_type=IamAdminService__pb2._REGISTERUSERSREQUEST,
    output_type=IamAdminService__pb2._REGISTERUSERSRESPONSE,
    serialized_options=b'\202\323\344\223\002&\"\035/user-management/v1.0.0/users:\005users',
  ),
  _descriptor.MethodDescriptor(
    name='addUserAttributes',
    full_name='org.apache.custos.user.management.service.UserManagementService.addUserAttributes',
    index=2,
    containing_service=None,
    input_type=IamAdminService__pb2._ADDUSERATTRIBUTESREQUEST,
    output_type=IamAdminService__pb2._OPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002$\"\"/user-management/v1.0.0/attributes',
  ),
  _descriptor.MethodDescriptor(
    name='deleteUserAttributes',
    full_name='org.apache.custos.user.management.service.UserManagementService.deleteUserAttributes',
    index=3,
    containing_service=None,
    input_type=IamAdminService__pb2._DELETEUSERATTRIBUTEREQUEST,
    output_type=IamAdminService__pb2._OPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002$*\"/user-management/v1.0.0/attributes',
  ),
  _descriptor.MethodDescriptor(
    name='enableUser',
    full_name='org.apache.custos.user.management.service.UserManagementService.enableUser',
    index=4,
    containing_service=None,
    input_type=IamAdminService__pb2._USERSEARCHREQUEST,
    output_type=IamAdminService__pb2._USERREPRESENTATION,
    serialized_options=b'\202\323\344\223\002/\"\'/user-management/v1.0.0/user/activation:\004user',
  ),
  _descriptor.MethodDescriptor(
    name='addRolesToUsers',
    full_name='org.apache.custos.user.management.service.UserManagementService.addRolesToUsers',
    index=5,
    containing_service=None,
    input_type=IamAdminService__pb2._ADDUSERROLESREQUEST,
    output_type=IamAdminService__pb2._OPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002%\"#/user-management/v1.0.0/users/roles',
  ),
  _descriptor.MethodDescriptor(
    name='isUserEnabled',
    full_name='org.apache.custos.user.management.service.UserManagementService.isUserEnabled',
    index=6,
    containing_service=None,
    input_type=IamAdminService__pb2._USERSEARCHREQUEST,
    output_type=IamAdminService__pb2._CHECKINGRESPONSE,
    serialized_options=b'\202\323\344\223\0020\022./user-management/v1.0.0/user/activation/status',
  ),
  _descriptor.MethodDescriptor(
    name='isUsernameAvailable',
    full_name='org.apache.custos.user.management.service.UserManagementService.isUsernameAvailable',
    index=7,
    containing_service=None,
    input_type=IamAdminService__pb2._USERSEARCHREQUEST,
    output_type=IamAdminService__pb2._CHECKINGRESPONSE,
    serialized_options=b'\202\323\344\223\002+\022)/user-management/v1.0.0/user/availability',
  ),
  _descriptor.MethodDescriptor(
    name='getUser',
    full_name='org.apache.custos.user.management.service.UserManagementService.getUser',
    index=8,
    containing_service=None,
    input_type=IamAdminService__pb2._USERSEARCHREQUEST,
    output_type=IamAdminService__pb2._USERREPRESENTATION,
    serialized_options=b'\202\323\344\223\002\036\022\034/user-management/v1.0.0/user',
  ),
  _descriptor.MethodDescriptor(
    name='findUsers',
    full_name='org.apache.custos.user.management.service.UserManagementService.findUsers',
    index=9,
    containing_service=None,
    input_type=IamAdminService__pb2._FINDUSERSREQUEST,
    output_type=IamAdminService__pb2._FINDUSERSRESPONSE,
    serialized_options=b'\202\323\344\223\002\037\022\035/user-management/v1.0.0/users',
  ),
  _descriptor.MethodDescriptor(
    name='resetPassword',
    full_name='org.apache.custos.user.management.service.UserManagementService.resetPassword',
    index=10,
    containing_service=None,
    input_type=IamAdminService__pb2._RESETUSERPASSWORD,
    output_type=IamAdminService__pb2._CHECKINGRESPONSE,
    serialized_options=b'\202\323\344\223\002\'\032%/user-management/v1.0.0/user/password',
  ),
  _descriptor.MethodDescriptor(
    name='deleteUser',
    full_name='org.apache.custos.user.management.service.UserManagementService.deleteUser',
    index=11,
    containing_service=None,
    input_type=IamAdminService__pb2._USERSEARCHREQUEST,
    output_type=IamAdminService__pb2._CHECKINGRESPONSE,
    serialized_options=b'\202\323\344\223\002$*\034/user-management/v1.0.0/user:\004user',
  ),
  _descriptor.MethodDescriptor(
    name='deleteUserRoles',
    full_name='org.apache.custos.user.management.service.UserManagementService.deleteUserRoles',
    index=12,
    containing_service=None,
    input_type=IamAdminService__pb2._DELETEUSERROLESREQUEST,
    output_type=IamAdminService__pb2._CHECKINGRESPONSE,
    serialized_options=b'\202\323\344\223\002$*\"/user-management/v1.0.0/user/roles',
  ),
  _descriptor.MethodDescriptor(
    name='updateUserProfile',
    full_name='org.apache.custos.user.management.service.UserManagementService.updateUserProfile',
    index=13,
    containing_service=None,
    input_type=_USERPROFILEREQUEST,
    output_type=UserProfileService__pb2._USERPROFILE,
    serialized_options=b'\202\323\344\223\0024\032$/user-management/v1.0.0/user/profile:\014user_profile',
  ),
  _descriptor.MethodDescriptor(
    name='getUserProfile',
    full_name='org.apache.custos.user.management.service.UserManagementService.getUserProfile',
    index=14,
    containing_service=None,
    input_type=_USERPROFILEREQUEST,
    output_type=UserProfileService__pb2._USERPROFILE,
    serialized_options=b'\202\323\344\223\002&\022$/user-management/v1.0.0/user/profile',
  ),
  _descriptor.MethodDescriptor(
    name='deleteUserProfile',
    full_name='org.apache.custos.user.management.service.UserManagementService.deleteUserProfile',
    index=15,
    containing_service=None,
    input_type=_USERPROFILEREQUEST,
    output_type=UserProfileService__pb2._USERPROFILE,
    serialized_options=b'\202\323\344\223\002&*$/user-management/v1.0.0/user/profile',
  ),
  _descriptor.MethodDescriptor(
    name='getAllUserProfilesInTenant',
    full_name='org.apache.custos.user.management.service.UserManagementService.getAllUserProfilesInTenant',
    index=16,
    containing_service=None,
    input_type=_USERPROFILEREQUEST,
    output_type=UserProfileService__pb2._GETALLUSERPROFILESRESPONSE,
    serialized_options=b'\202\323\344\223\002\'\022%/user-management/v1.0.0/users/profile',
  ),
  _descriptor.MethodDescriptor(
    name='getUserProfileAuditTrails',
    full_name='org.apache.custos.user.management.service.UserManagementService.getUserProfileAuditTrails',
    index=17,
    containing_service=None,
    input_type=UserProfileService__pb2._GETUPDATEAUDITTRAILREQUEST,
    output_type=UserProfileService__pb2._GETUPDATEAUDITTRAILRESPONSE,
    serialized_options=b'\202\323\344\223\002,\022*/user-management/v1.0.0/user/profile/audit',
  ),
])
_sym_db.RegisterServiceDescriptor(_USERMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['UserManagementService'] = _USERMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)