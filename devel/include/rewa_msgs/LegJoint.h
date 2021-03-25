// Generated by gencpp from file rewa_msgs/LegJoint.msg
// DO NOT EDIT!


#ifndef REWA_MSGS_MESSAGE_LEGJOINT_H
#define REWA_MSGS_MESSAGE_LEGJOINT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <rewa_msgs/Euler.h>
#include <rewa_msgs/Euler.h>
#include <rewa_msgs/Euler.h>

namespace rewa_msgs
{
template <class ContainerAllocator>
struct LegJoint_
{
  typedef LegJoint_<ContainerAllocator> Type;

  LegJoint_()
    : hip()
    , knee()
    , ankle()  {
    }
  LegJoint_(const ContainerAllocator& _alloc)
    : hip(_alloc)
    , knee(_alloc)
    , ankle(_alloc)  {
  (void)_alloc;
    }



   typedef  ::rewa_msgs::Euler_<ContainerAllocator>  _hip_type;
  _hip_type hip;

   typedef  ::rewa_msgs::Euler_<ContainerAllocator>  _knee_type;
  _knee_type knee;

   typedef  ::rewa_msgs::Euler_<ContainerAllocator>  _ankle_type;
  _ankle_type ankle;





  typedef boost::shared_ptr< ::rewa_msgs::LegJoint_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rewa_msgs::LegJoint_<ContainerAllocator> const> ConstPtr;

}; // struct LegJoint_

typedef ::rewa_msgs::LegJoint_<std::allocator<void> > LegJoint;

typedef boost::shared_ptr< ::rewa_msgs::LegJoint > LegJointPtr;
typedef boost::shared_ptr< ::rewa_msgs::LegJoint const> LegJointConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rewa_msgs::LegJoint_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rewa_msgs::LegJoint_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rewa_msgs::LegJoint_<ContainerAllocator1> & lhs, const ::rewa_msgs::LegJoint_<ContainerAllocator2> & rhs)
{
  return lhs.hip == rhs.hip &&
    lhs.knee == rhs.knee &&
    lhs.ankle == rhs.ankle;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rewa_msgs::LegJoint_<ContainerAllocator1> & lhs, const ::rewa_msgs::LegJoint_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rewa_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rewa_msgs::LegJoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rewa_msgs::LegJoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rewa_msgs::LegJoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rewa_msgs::LegJoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rewa_msgs::LegJoint_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rewa_msgs::LegJoint_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rewa_msgs::LegJoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8fda3c23f2e1e0ab3642357df5d5da86";
  }

  static const char* value(const ::rewa_msgs::LegJoint_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8fda3c23f2e1e0abULL;
  static const uint64_t static_value2 = 0x3642357df5d5da86ULL;
};

template<class ContainerAllocator>
struct DataType< ::rewa_msgs::LegJoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rewa_msgs/LegJoint";
  }

  static const char* value(const ::rewa_msgs::LegJoint_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rewa_msgs::LegJoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rewa_msgs/Euler hip\n"
"rewa_msgs/Euler knee\n"
"rewa_msgs/Euler ankle\n"
"\n"
"================================================================================\n"
"MSG: rewa_msgs/Euler\n"
"float64 r\n"
"float64 p\n"
"float64 y\n"
;
  }

  static const char* value(const ::rewa_msgs::LegJoint_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rewa_msgs::LegJoint_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.hip);
      stream.next(m.knee);
      stream.next(m.ankle);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LegJoint_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rewa_msgs::LegJoint_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rewa_msgs::LegJoint_<ContainerAllocator>& v)
  {
    s << indent << "hip: ";
    s << std::endl;
    Printer< ::rewa_msgs::Euler_<ContainerAllocator> >::stream(s, indent + "  ", v.hip);
    s << indent << "knee: ";
    s << std::endl;
    Printer< ::rewa_msgs::Euler_<ContainerAllocator> >::stream(s, indent + "  ", v.knee);
    s << indent << "ankle: ";
    s << std::endl;
    Printer< ::rewa_msgs::Euler_<ContainerAllocator> >::stream(s, indent + "  ", v.ankle);
  }
};

} // namespace message_operations
} // namespace ros

#endif // REWA_MSGS_MESSAGE_LEGJOINT_H