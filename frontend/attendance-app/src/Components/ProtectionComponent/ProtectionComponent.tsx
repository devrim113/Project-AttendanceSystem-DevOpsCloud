import { Outlet } from "react-router-dom";
import { getInformation } from "../../Helper/static";

type ProtectionComponentProps = {
    role: string;
};

export default function ProtectionComponent(props: ProtectionComponentProps) {
    let role = getInformation()["cognito:groups"] as string[];
    if (!(role.includes(props.role))) {
        if(role.includes("Students")) {
            window.location.href = "/"
            return (<></>);
        }
        window.location.href = `/${role[0].toLowerCase().slice(0, -1)}`
        return (<></>);
    }

    return (
        <Outlet />
    );
}