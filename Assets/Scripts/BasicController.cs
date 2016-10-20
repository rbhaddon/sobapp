using UnityEngine;
using System.Collections;

public class BasicController : MonoBehaviour {
	
	// Update is called once per frame
	void Update () {
		Debug.Log ("Horizontal Input = " + Input.GetAxis ("Horizontal"));
		Debug.Log ("Vertical Input = " + Input.GetAxis ("Vertical"));
	}
}
