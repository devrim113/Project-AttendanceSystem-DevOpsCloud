import { Outlet } from "react-router-dom";
import { getInformation } from "../../Helper/static";

type ProtectionComponentProps = {
    role: string;
};

/**
 * Renders the ProtectionComponent based on the user's role.
 * If the user's role does not match the required role, it redirects them to the appropriate page.
 * @param props - The component props containing the required role.
 * @returns The rendered ProtectionComponent or a redirect to the appropriate page.
 */
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