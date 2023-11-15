// Generated by gencpp from file basit_uygulamalar/CemberHareketResponse.msg
// DO NOT EDIT!


#ifndef BASIT_UYGULAMALAR_MESSAGE_CEMBERHAREKETRESPONSE_H
#define BASIT_UYGULAMALAR_MESSAGE_CEMBERHAREKETRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace basit_uygulamalar
{
template <class ContainerAllocator>
struct CemberHareketResponse_
{
  typedef CemberHareketResponse_<ContainerAllocator> Type;

  CemberHareketResponse_()
    : stop(false)  {
    }
  CemberHareketResponse_(const ContainerAllocator& _alloc)
    : stop(false)  {
  (void)_alloc;
    }



   typedef uint8_t _stop_type;
  _stop_type stop;





  typedef boost::shared_ptr< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> const> ConstPtr;

}; // struct CemberHareketResponse_

typedef ::basit_uygulamalar::CemberHareketResponse_<std::allocator<void> > CemberHareketResponse;

typedef boost::shared_ptr< ::basit_uygulamalar::CemberHareketResponse > CemberHareketResponsePtr;
typedef boost::shared_ptr< ::basit_uygulamalar::CemberHareketResponse const> CemberHareketResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator1> & lhs, const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator2> & rhs)
{
  return lhs.stop == rhs.stop;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator1> & lhs, const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace basit_uygulamalar

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "71f1172402e56b82716ca71681cded6b";
  }

  static const char* value(const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x71f1172402e56b82ULL;
  static const uint64_t static_value2 = 0x716ca71681cded6bULL;
};

template<class ContainerAllocator>
struct DataType< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "basit_uygulamalar/CemberHareketResponse";
  }

  static const char* value(const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool stop\n"
"\n"
;
  }

  static const char* value(const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.stop);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CemberHareketResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::basit_uygulamalar::CemberHareketResponse_<ContainerAllocator>& v)
  {
    s << indent << "stop: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.stop);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BASIT_UYGULAMALAR_MESSAGE_CEMBERHAREKETRESPONSE_H
