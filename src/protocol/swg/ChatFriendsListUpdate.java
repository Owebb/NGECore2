package protocol.swg;

import java.nio.ByteOrder;

import main.NGECore;

import org.apache.mina.core.buffer.IoBuffer;

import engine.resources.config.Config;
import engine.resources.config.DefaultConfig;

public class ChatFriendsListUpdate extends SWGMessage {

	
	private NGECore core;
	private String friendName;
	private byte onlineFlag;

	// FriendStatusChangeMessage
	// online/offline messages
	public ChatFriendsListUpdate(String friendName, byte onlineFlag) {
		this.friendName = friendName;
		this.onlineFlag = onlineFlag;
	}
	
	@Override
	public void deserialize(IoBuffer data) {
		
		
	}

	@Override
	public IoBuffer serialize() {
		Config config = new Config();
		config.setFilePath("nge.cfg");
		if (!(config.loadConfigFile())) {
			config = DefaultConfig.getConfig();
		}
		String serverName = config.getString("GALAXY_NAME");
		
		IoBuffer result = IoBuffer.allocate(50 + friendName.length()).order(ByteOrder.LITTLE_ENDIAN);
		result.putShort((short) 3);
		result.putInt(0x6CD2FCD8);
		result.put(getAsciiString("SWG"));
		result.put(getAsciiString(serverName));
		result.put(getAsciiString(friendName));
		result.put(onlineFlag);
		result.flip();
		//System.out.println("ChatFriendsListUpdate: " + result.getHexDump());
		return result;
	}

}
