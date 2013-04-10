#include "stdafx.h"
#include "UIMessageBox.h"


UIMessageBox::UIMessageBox(void)
{
}


UIMessageBox::~UIMessageBox(void)
{
}

void UIMessageBox::display(std::string title, std::string message)
{
	MessageBoxA(NULL, message.c_str(), title.c_str(), MB_OKCANCEL);
}