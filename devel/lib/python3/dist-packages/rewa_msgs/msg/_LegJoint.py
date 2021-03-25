# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rewa_msgs/LegJoint.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rewa_msgs.msg

class LegJoint(genpy.Message):
  _md5sum = "8fda3c23f2e1e0ab3642357df5d5da86"
  _type = "rewa_msgs/LegJoint"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """rewa_msgs/Euler hip
rewa_msgs/Euler knee
rewa_msgs/Euler ankle

================================================================================
MSG: rewa_msgs/Euler
float64 r
float64 p
float64 y
"""
  __slots__ = ['hip','knee','ankle']
  _slot_types = ['rewa_msgs/Euler','rewa_msgs/Euler','rewa_msgs/Euler']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       hip,knee,ankle

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LegJoint, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.hip is None:
        self.hip = rewa_msgs.msg.Euler()
      if self.knee is None:
        self.knee = rewa_msgs.msg.Euler()
      if self.ankle is None:
        self.ankle = rewa_msgs.msg.Euler()
    else:
      self.hip = rewa_msgs.msg.Euler()
      self.knee = rewa_msgs.msg.Euler()
      self.ankle = rewa_msgs.msg.Euler()

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
      buff.write(_get_struct_9d().pack(_x.hip.r, _x.hip.p, _x.hip.y, _x.knee.r, _x.knee.p, _x.knee.y, _x.ankle.r, _x.ankle.p, _x.ankle.y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.hip is None:
        self.hip = rewa_msgs.msg.Euler()
      if self.knee is None:
        self.knee = rewa_msgs.msg.Euler()
      if self.ankle is None:
        self.ankle = rewa_msgs.msg.Euler()
      end = 0
      _x = self
      start = end
      end += 72
      (_x.hip.r, _x.hip.p, _x.hip.y, _x.knee.r, _x.knee.p, _x.knee.y, _x.ankle.r, _x.ankle.p, _x.ankle.y,) = _get_struct_9d().unpack(str[start:end])
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
      buff.write(_get_struct_9d().pack(_x.hip.r, _x.hip.p, _x.hip.y, _x.knee.r, _x.knee.p, _x.knee.y, _x.ankle.r, _x.ankle.p, _x.ankle.y))
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
      if self.hip is None:
        self.hip = rewa_msgs.msg.Euler()
      if self.knee is None:
        self.knee = rewa_msgs.msg.Euler()
      if self.ankle is None:
        self.ankle = rewa_msgs.msg.Euler()
      end = 0
      _x = self
      start = end
      end += 72
      (_x.hip.r, _x.hip.p, _x.hip.y, _x.knee.r, _x.knee.p, _x.knee.y, _x.ankle.r, _x.ankle.p, _x.ankle.y,) = _get_struct_9d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_9d = None
def _get_struct_9d():
    global _struct_9d
    if _struct_9d is None:
        _struct_9d = struct.Struct("<9d")
    return _struct_9d
