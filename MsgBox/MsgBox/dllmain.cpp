// dllmain.cpp : Defines the entry point for the DLL application.
#include "stdafx.h"
#include "UIMessageBox.h"

void displayMessage() 
{
	UIMessageBox msgbox = UIMessageBox();
	msgbox.display("DLL Injection", "Hello World!");
}

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
					 )
{
	switch (ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
		displayMessage();
	case DLL_THREAD_ATTACH:

	case DLL_THREAD_DETACH:

	case DLL_PROCESS_DETACH:
		break;
	}
	return TRUE;
}

