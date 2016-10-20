using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using System.Collections;

public class DragUI : MonoBehaviour, IPointerDownHandler, IPointerUpHandler {

	private bool mouseDown = false;
	private Vector3 startMousePos;
	private Vector3 startPos;


	public void OnPointerDown(PointerEventData ped) 
	{
		mouseDown = true;
		startPos = transform.position;
		startMousePos = Input.mousePosition;
	}

	public void OnPointerUp(PointerEventData ped) 
	{
		mouseDown = false;
	}


	void Update () 
	{
		if (mouseDown) {
			Vector3 currentPos = Input.mousePosition;
			Vector3 diff = currentPos - startMousePos;
			Vector3 pos = startPos + diff;
			transform.position = pos;
		}
	}
}
