# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rewa_msgs/EulerAngle.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class EulerAngle(genpy.Message):
  _md5sum = "b12334b058a796e17415fad4ae059df8"
  _type = "rewa_msgs/EulerAngle"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Float32 r
std_msgs/Float32 p
std_msgs/Float32 y

================================================================================
MSG: std_msgs/Float32
float32 data"""
  __slots__ = ['r','p','y']
  _slot_types = ['std_msgs/Float32','std_msgs/Float32','std_msgs/Float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       r,p,y

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EulerAngle, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.r is None:
        self.r = std_msgs.msg.Float32()
      if self.p is None:
        self.p = std_msgs.msg.Float32()
      if self.y is None:
        self.y = std_msgs.msg.Float32()
    else:
      self.r = std_msgs.msg.Float32()
      self.p = std_msgs.msg.Float32()
      self.y = std_msgs.msg.Float32()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3f().pack(_x.r.data, _x.p.data, _x.y.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.r is None:
        self.r = std_msgs.msg.Float32()
      if self.p is None:
        self.p = std_msgs.msg.Float32()
      if self.y is None:
        self.y = std_msgs.msg.Float32()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.r.data, _x.p.data, _x.y.data,) = _get_struct_3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3f().pack(_x.r.data, _x.p.data, _x.y.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.r is None:
        self.r = std_msgs.msg.Float32()
      if self.p is None:
        self.p = std_msgs.msg.Float32()
      if self.y is None:
        self.y = std_msgs.msg.Float32()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.r.data, _x.p.data, _x.y.data,) = _get_struct_3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f