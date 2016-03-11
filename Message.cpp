#include "Message.h"

#include <stdio.h>
#include <stdlib.h>
#include <map>
using namespace std;

int main()
{
	Message msg;
	map<U32, Message*> map0;
	for (int loop = 0; loop < MAX_NUM; loop++)
	{
		memset(msg.data, 0, sizeof(msg.data));
		msg.msgBrief.msgid = loop;
		msg.msgBrief.length = MAX_NUM;
		msg.msgBrief.priority = 0;
		msg.msgBrief.version = 0;
		map0.insert(pair<U32, Message*> (loop, &msg));
	}
	
	system("pause");
	return 0;
}
