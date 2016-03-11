#ifndef MESSAGE_H
#define MESSAGE_H

typedef unsigned char U8;
typedef unsigned int U32;
#define MAX_EVENT_LEN 20
#define MAX_NUM 10

typedef union Elem
{
	U32 v;
	void* p;
} Elem;

struct MsgBrief
{
	U32 version;
	U32 msgid;
	U32 length;
	U32 priority;
};

struct Message
{
	MsgBrief msgBrief;
	U8 data[MAX_EVENT_LEN];
};

struct MsgComparator
{
	bool operatorfunc(Message first, Message second);
};

#endif
