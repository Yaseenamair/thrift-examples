#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport


class Iface(object):
    def ping(self):
        pass

    def say(self, msg):
        """
        Parameters:
         - msg
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def ping(self):
        self.send_ping()
        return self.recv_ping()

    def send_ping(self):
        self._oprot.writeMessageBegin('ping', TMessageType.CALL, self._seqid)
        args = ping_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ping(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ping_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "ping failed: unknown result")

    def say(self, msg):
        """
        Parameters:
         - msg
        """
        self.send_say(msg)
        self.recv_say()

    def send_say(self, msg):
        self._oprot.writeMessageBegin('say', TMessageType.CALL, self._seqid)
        args = say_args()
        args.msg = msg
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_say(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = say_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["ping"] = Processor.process_ping
        self._processMap["say"] = Processor.process_say

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_ping(self, seqid, iprot, oprot):
        args = ping_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ping_result()
        try:
            result.success = self._handler.ping()
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("ping", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_say(self, seqid, iprot, oprot):
        args = say_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = say_result()
        try:
            self._handler.say(args.msg)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("say", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class ping_args(object):

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ping_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ping_result(object):
    """
    Attributes:
     - success
    """

    thrift_spec = (
        (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ping_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class say_args(object):
    """
    Attributes:
     - msg
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'msg', 'UTF8', None, ),  # 1
    )

    def __init__(self, msg=None,):
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('say_args')
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 1)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class say_result(object):

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('say_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
