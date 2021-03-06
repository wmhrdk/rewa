# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rewa_msgs/WalkOutput.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rewa_msgs.msg

class WalkOutput(genpy.Message):
  _md5sum = "9ad5775b0d561da386890fe8cd014165"
  _type = "rewa_msgs/WalkOutput"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """rewa_msgs/LegJoint left
rewa_msgs/LegJoint right

================================================================================
MSG: rewa_msgs/LegJoint
rewa_msgs/Euler hip
rewa_msgs/Euler knee
rewa_msgs/Euler ankle

================================================================================
MSG: rewa_msgs/Euler
float64 r
float64 p
float64 y
"""
  __slots__ = ['left','right']
  _slot_types = ['rewa_msgs/LegJoint','rewa_msgs/LegJoint']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       left,right

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WalkOutput, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.left is None:
        self.left = rewa_msgs.msg.LegJoint()
      if self.right is None:
        self.right = rewa_msgs.msg.LegJoint()
    else:
      self.left = rewa_msgs.msg.LegJoint()
      self.right = rewa_msgs.msg.LegJoint()

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
      buff.write(_get_struct_18d().pack(_x.left.hip.r, _x.left.hip.p, _x.left.hip.y, _x.left.knee.r, _x.left.knee.p, _x.left.knee.y, _x.left.ankle.r, _x.left.ankle.p, _x.left.ankle.y, _x.right.hip.r, _x.right.hip.p, _x.right.hip.y, _x.right.knee.r, _x.right.knee.p, _x.right.knee.y, _x.right.ankle.r, _x.right.ankle.p, _x.right.ankle.y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.left is None:
        self.left = rewa_msgs.msg.LegJoint()
      if self.right is None:
        self.right = rewa_msgs.msg.LegJoint()
      end = 0
      _x = self
      start = end
      end += 144
      (_x.left.hip.r, _x.left.hip.p, _x.left.hip.y, _x.left.knee.r, _x.left.knee.p, _x.left.knee.y, _x.left.ankle.r, _x.left.ankle.p, _x.left.ankle.y, _x.right.hip.r, _x.right.hip.p, _x.right.hip.y, _x.right.knee.r, _x.right.knee.p, _x.right.knee.y, _x.right.ankle.r, _x.right.ankle.p, _x.right.ankle.y,) = _get_struct_18d().unpack(str[start:end])
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
      buff.write(_get_struct_18d().pack(_x.left.hip.r, _x.left.hip.p, _x.left.hip.y, _x.left.knee.r, _x.left.knee.p, _x.left.knee.y, _x.left.ankle.r, _x.left.ankle.p, _x.left.ankle.y, _x.right.hip.r, _x.right.hip.p, _x.right.hip.y, _x.right.knee.r, _x.right.knee.p, _x.right.knee.y, _x.right.ankle.r, _x.right.ankle.p, _x.right.ankle.y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.left is None:
        self.left = rewa_msgs.msg.LegJoint()
      if self.right is None:
        self.right = rewa_msgs.msg.LegJoint()
      end = 0
      _x = self
      start = end
      end += 144
      (_x.left.hip.r, _x.left.hip.p, _x.left.hip.y, _x.left.knee.r, _x.left.knee.p, _x.left.knee.y, _x.left.ankle.r, _x.left.ankle.p, _x.left.ankle.y, _x.right.hip.r, _x.right.hip.p, _x.right.hip.y, _x.right.knee.r, _x.right.knee.p, _x.right.knee.y, _x.right.ankle.r, _x.right.ankle.p, _x.right.ankle.y,) = _get_struct_18d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_18d = None
def _get_struct_18d():
    global _struct_18d
    if _struct_18d is None:
        _struct_18d = struct.Struct("<18d")
    return _struct_18d
