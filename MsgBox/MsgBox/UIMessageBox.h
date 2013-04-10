#pragma once

#include <string>

class UIMessageBox
{
public:
	UIMessageBox(void);
	~UIMessageBox(void);

	void display(std::string, std::string);
};

