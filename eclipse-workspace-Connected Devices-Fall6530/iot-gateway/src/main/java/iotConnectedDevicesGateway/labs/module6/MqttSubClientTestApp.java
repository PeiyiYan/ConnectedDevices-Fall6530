package iotConnectedDevicesGateway.labs.module6;
import java.util.logging.Logger;

public class MqttSubClientTestApp
{
// static
	private static final Logger _Logger = Logger.getLogger(MqttSubClientTestApp.class.getName());
	private static MqttSubClientTestApp _App;
/**
* @param args
*/
	public static void main(String[] args)
	{
		_App = new MqttSubClientTestApp();
		try {
			_App.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
// params
	private MqttClientConnector _mqttClient;
// constructors
/**
* Default.
*/
	public MqttSubClientTestApp()
	{
		super();
	}
// public methods
/**
* Connect to the MQTT client, then:
*/
	public void start()
	{
		_mqttClient = new MqttClientConnector("tcp","test.mosquitto.org",1883);
		_mqttClient.connect();
		String topicName = "ConnectedDevicesMQTT";

		_mqttClient.subscribeToTopic(topicName,2); 
		//_mqttClient.subscribeToAll(); 
		/**We do not need to subscribe to all topic otherwise we would get lots of logging.
		 */
		//_mqttClient.disconnect();
	}
}