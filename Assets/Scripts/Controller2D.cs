using UnityEngine;
using System.Collections;

public class Controller2D : MonoBehaviour {
	
	// public variables
	public float moveSpeed = 3.0f;

	private CharacterController myController;

	// Use this for initialization
	void Start () {
		// store a reference to the CharacterController component on this gameObject
		// it is much more efficient to use GetComponent() once in Start and store
		// the result rather than continually use etComponent() in the Update function
		myController = gameObject.GetComponent<CharacterController>();
	}
	
	// Update is called once per frame
	void Update () {
		// Determine how much should move in the y-direction
		Vector2 movementY = Input.GetAxis ("Vertical") * Vector2.up * moveSpeed * Time.deltaTime;

		// Determine how much should move in the x-direction
		Vector2 movementX = Input.GetAxis ("Horizontal") * Vector2.right * moveSpeed * Time.deltaTime;

		// Convert combined Vector2 from local space to world space based on the position of the current gameobject (player)
		Vector2 movement = transform.TransformDirection (movementY + movementX);

		//Debug.Log ("Movement Vector = " + movement);

		// Actually move the character controller in the movement direction
		myController.Move(movement);
	}
}