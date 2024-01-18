package com.example.userservice;

import com.example.domain.User;

public interface UserUserService {
    
    User selectByNum(String memberId);
	
	Integer write(User dto);
	
	Integer update(User dto);

}